import os
import json
import server
from aiohttp import web

print("✅ [ZML-Patch] INIT: Loading web assets and translation API...")

WEB_DIRECTORY = "./js"
zml_translation_map = {}

@server.PromptServer.instance.routes.get("/zml/get_translation")
async def get_zml_translation(request):
    return web.json_response(zml_translation_map)

# --- 修改过的函数 ---
def load_translation_file():
    """
    自动扫描当前目录下的所有 .json 文件，并将它们合并。
    """
    global zml_translation_map
    
    # 初始化一个标准的、空的翻译结构
    merged_map = {
        "NODE_DISPLAY_NAME_MAPPINGS": {},
        "UI_TEXT": {}
    }
    loaded_files = []
    
    p = os.path.dirname(os.path.realpath(__file__))
    
    try:
        # 遍历目录中的所有文件
        for filename in os.listdir(p):
            # 如果文件以 .json 结尾（不区分大小写）
            if filename.lower().endswith('.json'):
                file_path = os.path.join(p, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        
                        # 合并 NODE_DISPLAY_NAME_MAPPINGS
                        if "NODE_DISPLAY_NAME_MAPPINGS" in data:
                            merged_map["NODE_DISPLAY_NAME_MAPPINGS"].update(data.get("NODE_DISPLAY_NAME_MAPPINGS", {}))
                        
                        # 合并 UI_TEXT
                        if "UI_TEXT" in data:
                            merged_map["UI_TEXT"].update(data.get("UI_TEXT", {}))
                        
                        loaded_files.append(filename)
                except Exception as e:
                    print(f"❌ [ZML-Patch] ERROR: Failed to load or parse '{filename}': {e}")

        if loaded_files:
            zml_translation_map = merged_map
            print(f"✅ [ZML-Patch] SUCCESS: Loaded {len(loaded_files)} translation file(s): {sorted(loaded_files)}")
        else:
            print("❌ [ZML-Patch] WARNING: No translation files (.json) found in the directory.")
            
    except Exception as e:
        print(f"❌ [ZML-Patch] ERROR: An unexpected error occurred while scanning for translation files: {e}")


load_translation_file()

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}