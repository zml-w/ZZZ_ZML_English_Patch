import { app } from "/scripts/app.js";

let ZML_TRANSLATIONS = {
    NODE_DISPLAY_NAME_MAPPINGS: {},
    UI_TEXT: {},
};

function T(text) {
    if (!text) return text;
    const trimmedText = text.trim();
    if (ZML_TRANSLATIONS.UI_TEXT[trimmedText]) {
        return ZML_TRANSLATIONS.UI_TEXT[trimmedText];
    }
    if (ZML_TRANSLATIONS.NODE_DISPLAY_NAME_MAPPINGS[trimmedText]) {
        return ZML_TRANSLATIONS.NODE_DISPLAY_NAME_MAPPINGS[trimmedText];
    }
    return trimmedText;
}

function applyNodeTranslation(node) {
    if (!node || !node.title || !node.title.toLowerCase().startsWith("zml")) return;

    node.title = T(node.title);

    if (node.inputs) {
        node.inputs.forEach(input => {
            const originalLabel = input.label || input.name;
            input.label = T(originalLabel);
        });
    }

    if (node.outputs) {
        node.outputs.forEach(output => {
            const originalName = output.name;
            output.name = T(originalName);
            output.label = T(originalName);
        });
    }

    if (node.widgets) {
        node.widgets.forEach(widget => {
            const originalLabel = widget.label || widget.name;
            if(originalLabel) widget.label = T(originalLabel);
        });
    }
    node.setDirtyCanvas(true, true);
}


const ZmlPatcher = {
    name: "ZML.Patcher.zh-CN_to_EN.Final.v2",
    async setup() {
        try {
            const response = await fetch("/zml/get_translation");
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            const data = await response.json();
            if (data && data.UI_TEXT) {
                ZML_TRANSLATIONS = data;
                console.log("ZML Patcher: Translations loaded successfully.");
                
                // --- 关键修改：改进分类翻译的逻辑 ---
                for (const nodeClassName in LiteGraph.registered_node_types) {
                    if (nodeClassName.toLowerCase().startsWith("zml")) {
                        const nodeDef = LiteGraph.registered_node_types[nodeClassName];
                        if (nodeDef) {
                            // 翻译菜单中的节点标题
                            nodeDef.title = T(nodeDef.title);
                            
                            // 翻译菜单中的分类 (拆分路径，分别翻译每一部分)
                            const originalCategory = nodeDef.category;
                            if (typeof originalCategory === 'string' && originalCategory.includes('/')) {
                                const parts = originalCategory.split('/');
                                const translatedParts = parts.map(part => T(part));
                                nodeDef.category = translatedParts.join('/');
                            } else {
                                nodeDef.category = T(originalCategory);
                            }
                        }
                    }
                }

            } else {
                console.warn("ZML Patcher: Fetched translation data is invalid or empty.");
            }
        } catch (e) {
            console.error("ZML Patcher: Failed to load translations from backend.", e);
        }
    },
    
    nodeCreated(node) {
        setTimeout(() => applyNodeTranslation(node), 0);
    },
};

app.registerExtension(ZmlPatcher);