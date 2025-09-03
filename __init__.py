# This robust patcher loads translations from all .json files
# found within its own directory, merging them to apply the patch.
# Version 4.0: Corrects a scope/timing issue where the argument translation map was created before being populated.

import json
import os
import copy

# --- 配置开关 ---
ENABLE_PATCH_LOGGING = False

# --- 加载ComfyUI核心注册表 ---
try:
    from comfy.sd import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    try:
        from nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
    except ImportError:
        print("❌ [ZML English Patch] Could not import ComfyUI node registries.")
        NODE_CLASS_MAPPINGS = {}
        NODE_DISPLAY_NAME_MAPPINGS = {}

def log(message):
    if ENABLE_PATCH_LOGGING:
        print(f"💡 [ZML English Patch] {message}")

def create_argument_wrapper(original_function, translation_map):
    """
    创建一个包装函数，接收英文关键字参数，翻译回中文，然后调用原始函数。
    """
    def wrapper(self, **kwargs):
        translated_kwargs = {}
        for key, value in kwargs.items():
            chinese_key = translation_map.get(key, key)
            translated_kwargs[chinese_key] = value
        return original_function(self, **translated_kwargs)
    return wrapper

def apply_zml_translation_patch():
    if not NODE_CLASS_MAPPINGS:
        return

    log("Scanning for translation files...")
    patch_dir = os.path.dirname(__file__)
    all_translations = {"NODE_DISPLAY_NAME_MAPPINGS": {}, "UI_TEXT": {}}
    
    json_files_found = []
    for filename in os.listdir(patch_dir):
        if filename.lower().endswith(".json"):
            json_path = os.path.join(patch_dir, filename)
            json_files_found.append(filename)
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    all_translations["NODE_DISPLAY_NAME_MAPPINGS"].update(data.get("NODE_DISPLAY_NAME_MAPPINGS", {}))
                    all_translations["UI_TEXT"].update(data.get("UI_TEXT", {}))
            except Exception as e:
                print(f"❌ [ZML English Patch] ERROR: Failed to load or parse {filename}: {e}")

    if not json_files_found:
        log("No .json files found. Aborting.")
        return
        
    log(f"Loaded translations from: {', '.join(sorted(json_files_found))}")

    translated_display_names = all_translations.get("NODE_DISPLAY_NAME_MAPPINGS", {})
    ui_text_map = all_translations.get("UI_TEXT", {})

    def translate(text):
        return ui_text_map.get(str(text), text)

    # 翻译节点显示名称
    for key, value in NODE_DISPLAY_NAME_MAPPINGS.items():
        if key.lower().startswith("zml") and value in translated_display_names:
            NODE_DISPLAY_NAME_MAPPINGS[key] = translated_display_names[value]

    # 翻译节点内部参数
    for node_identifier, node_class in NODE_CLASS_MAPPINGS.items():
        if not node_identifier.lower().startswith("zml"):
            continue
        try:
            if hasattr(node_class, "CATEGORY"): node_class.CATEGORY = translate(node_class.CATEGORY)
            if hasattr(node_class, "RETURN_NAMES"): node_class.RETURN_NAMES = tuple(translate(name) for name in node_class.RETURN_NAMES)
            
            # --- 核心逻辑修正 ---
            # 必须先构建参数映射，然后再用这个映射去创建包装器和新的INPUT_TYPES
            if hasattr(node_class, "INPUT_TYPES"):
                original_inputs = node_class.INPUT_TYPES()
                arg_translation_map = {} # { "EnglishName": "中文名" }

                # 1. 首先，立即构建参数翻译字典
                for i_type in ['required', 'optional', 'hidden']:
                    if i_type in original_inputs:
                        for chinese_name in original_inputs[i_type]:
                            english_name = translate(chinese_name)
                            arg_translation_map[english_name] = chinese_name
                
                # 2. 然后，使用这个已经填充好的字典来创建包装函数
                if hasattr(node_class, "FUNCTION"):
                    original_func_name = node_class.FUNCTION
                    if hasattr(node_class, original_func_name):
                        original_function = getattr(node_class, original_func_name)
                        wrapper_function = create_argument_wrapper(original_function, arg_translation_map)
                        setattr(node_class, original_func_name, wrapper_function)
                
                # 3. 最后，创建并替换 INPUT_TYPES 方法用于UI显示
                @classmethod
                def patched_input_types(cls, inputs_to_patch=copy.deepcopy(original_inputs)):
                    patched_inputs = inputs_to_patch
                    for i_type in ['required', 'optional', 'hidden']:
                        if i_type in patched_inputs:
                            translated_section = {}
                            for name, config in patched_inputs[i_type].items():
                                t_name = translate(name)
                                if isinstance(config, tuple) and len(config) > 0 and isinstance(config[0], list):
                                    config_list = list(config)
                                    config_list[0] = [translate(item) for item in config_list[0]]
                                    translated_section[t_name] = tuple(config_list)
                                else:
                                    translated_section[t_name] = config
                            patched_inputs[i_type] = translated_section
                    return patched_inputs
                
                node_class.INPUT_TYPES = patched_input_types

        except Exception as e:
            print(f"❌ [ZML English Patch] ERROR: Failed to patch class {node_class.__name__}: {e}")

    log("ZML translation patch applied successfully.")

# --- 主执行代码 ---
apply_zml_translation_patch()
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}