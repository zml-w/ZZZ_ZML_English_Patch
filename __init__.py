
import json
import os
import copy

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
    """根据开关状态决定是否打印日志的辅助函数"""
    if ENABLE_PATCH_LOGGING:
        print(f"💡 [ZML English Patch] {message}")

def apply_zml_translation_patch():
    if not NODE_CLASS_MAPPINGS:
        return

    log("Scanning for translation files in patch directory...")
    
    patch_dir = os.path.dirname(__file__)
    all_translations = {
        "NODE_DISPLAY_NAME_MAPPINGS": {},
        "UI_TEXT": {}
    }
    
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
                # 错误信息
                print(f"❌ [ZML English Patch] ERROR: Failed to load or parse {filename}: {e}")

    if not json_files_found:
        log("No .json translation files found in the patch directory. Aborting.")
        return
        
    log(f"Loaded translations from: {', '.join(sorted(json_files_found))}")

    translated_display_names = all_translations.get("NODE_DISPLAY_NAME_MAPPINGS", {})
    ui_text_map = all_translations.get("UI_TEXT", {})

    def translate(text):
        return ui_text_map.get(str(text), text)

    for key, value in NODE_DISPLAY_NAME_MAPPINGS.items():
        if key.lower().startswith("zml") and value in translated_display_names:
            NODE_DISPLAY_NAME_MAPPINGS[key] = translated_display_names[value]

    for node_identifier, node_class in NODE_CLASS_MAPPINGS.items():
        if not node_identifier.lower().startswith("zml"):
            continue
        try:
            if hasattr(node_class, "CATEGORY"): node_class.CATEGORY = translate(node_class.CATEGORY)
            if hasattr(node_class, "RETURN_NAMES"): node_class.RETURN_NAMES = tuple(translate(name) for name in node_class.RETURN_NAMES)
            if hasattr(node_class, "INPUT_TYPES"):
                original_method = node_class.INPUT_TYPES
                @classmethod
                def patched_method(cls, o_method=original_method):
                    original_inputs = o_method()
                    patched_inputs = copy.deepcopy(original_inputs)
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
                node_class.INPUT_TYPES = patched_method
        except Exception as e:
            print(f"❌ [ZML English Patch] ERROR: Failed to patch class {node_class.__name__}: {e}")

    log("ZML translation patch applied successfully.")


# --- 主执行代码 ---
apply_zml_translation_patch()
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}