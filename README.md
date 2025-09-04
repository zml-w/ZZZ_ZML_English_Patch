<div align="center">
  
## The patch file needs to be used with ComfyUI-ZML-Image. 

# [Click here to download](https://github.com/zml-w/ComfyUI-ZML-Image)

</div>

# ZZZ_ZML_English_Patch
- ### ComfyUI-ZML-Image English translation patch

- ### The documentation was translated by AI.

- ### Simply place the patch file in the same directory to use it!

- ### The name must remain "ZZZ_ZML_English_Patch"!

- ### Except for the drop-down options and the nodes with UI interfaces written in JS, everything else has been translated normally!

<img width="807" height="77" alt="屏幕截图 2025-09-03 124948" src="https://github.com/user-attachments/assets/5ff21b5f-12f5-4946-bc57-a97922dd2374" />

# 💕 Brief Introduction to the Nodes:
**This is a feature-rich COMFYUI custom node pack, mainly related to “Image, Text, Integer, LoRA Loader, Mask”, along with some miscellaneous small tools. Currently, there are 50+ nodes in total, and generally, new nodes are added every two days.**

`I developed these according to my own needs.`

`Some nodes have a “help” output interface, which contains detailed introductions of the nodes. If a node does not have help and you don’t know how to use it, you can check the previous version update notes.`

`All node names start with “ZML_” and are all placed under the “Image/ZML_Image” category.`

## ✨ Version Update Notes

> ### Latest Update Date: **2025.09.04**

> - #### The Tagged Image Selection Node can now remember the last opened location, so you no longer have to search for subfolders every time you open it.
>
> - #### Removed the regular LORA loading node.
>
> - #### When parsing LORA metadata and fetching C-site information for powerful LORAs, if a "wan" LORA is encountered, both the MP4 and the initial frame will now be saved simultaneously.
> 
> - #### The powerful LORA Loader node, and the batch add LORA page, now support MP4 playback!!
>
> - #### There are also some minor optimizations, which won't be detailed here.

<details>
  
> ### Update Date: **2025.09.03**
>
> - #### Fixed a minor bug in the Random Text Weight node.
>
> - #### Fixed a bug where the Save Image node could not preview images.
>
> - #### Added diagonal mask support to the Mask Split node.
> 
> - #### Removed the GIF File Path node and added a Load Video from Path node, which also supports loading GIFs.
>
> - #### Optimized the Text Format Conversion node. Now, in addition to converting NAI weights to SD, it also supports clearing all weights in one click (both NAI and SD). It also supports appending spaces after commas in prompts. Removed help text (punctuation normalization replaces non-standard commas, periods, and the “BREAK” syntax with SDXL-compatible syntax).
>
> - #### Added the Limit Image Ratio node, which can pad or crop images to a specified ratio. Later, you can use the Limit Solid Background node to remove the padding background.
>
> - #### Optimized the Powerful LoRA Loader node, mainly its UI for batch loading LoRAs.
>
>   * In addition to square previews, it now supports vertical and horizontal previews.
>   * You can view and edit txt and log files (trigger words and descriptions) in real-time, and also delete LoRAs and related files with one click. Deleted LoRAs will be labeled “Deleted” to prevent incorrect loading.
>

<summary>Click to view more past updates</summary>

> ### Update Date: **2025.09.02**
>
> - #### Fixed an issue where the Powerful LoRA node could not be used due to a missing punctuation mark.
>   
> - #### Added the Limit Mask Shape node.
>   
> - #### Fixed a bug where the Desktop Pet could not load properly.
>   
> - #### Optimized the Tagged Prompt Loader.
>   
> - #### The Drawing node added several preset colors and optimized UI and usability.
>   
> - #### Optimized the Tagged Image Loader node.
>

> ### Update Date: **2025.08.27**
>
> - #### Fixed a bug in the Powerful LoRA Loader code that caused UI issues in ComfyUI settings page.
>   
> - #### Fixed an issue where the Auto-Censor node sometimes could not read the YOLO model.
>   
> - #### Added a YOLO-to-Mask node.
>   
> - #### Optimized Preset Resolution and Preset Text nodes.
>   
> - #### Added a Mask Separation node, which can split one mask into two or three masks (useful for conditional partitioning, e.g., YOLO auto-detection for face retouching).
>   
> - #### Added a Unified Image Resolution node.
>   
> - #### Desktop Pet now supports chatting! Right-click to select Chat Mode and enter your Google API key in settings.
>   
>   * Added feeding function! Buy food in the store and feed the little sister! With subtitles and sound effects!
>     
>   * Added a countdown timer function.
>     
>   * You can replace Desktop Pet’s assets (sound effects/images) by replacing files in `ComfyUI-ZML-Image\zml_w\web\images`.
>     
>   * If you don’t like Desktop Pet, right-click to hide it or delete `ComfyUI-ZML-Image\zml_w\web\js\zml_floating_ball.js`.
>     

> ### Update Date: **2025.08.27**
>
> - #### Optimized Mask Split node.
>   
> - #### Major update to the Drawing node: now supports drawing on input images, drawing mosaics, and simple shapes (“Square, Triangle, Circle, Heart, Pentagon, Arrow”).
>   
> - #### Added Image Deformation node (simulates liquify/warp in Photoshop, transparency not supported yet).
>   
> - #### Custom text input boxes in Select Text V3 and Powerful LoRA Loader nodes changed to read-only. Click to open popup window for easier editing.
>   
> - #### Fixed a bug where Powerful LoRA Loader node required a CLIP connection. Now it’s optional.
>   
> - #### Added a popup window in Powerful LoRA Loader node for batch adding LoRAs, with one-click LoRA info fetching. Buttons now have CSS visual feedback.
>   
> - #### Added Categorize Images node, which classifies images into “No Metadata, With Metadata, With Text Blocks”. Example workflow uploaded.
>   
> - #### Added Name-Based LoRA Loader node. Powerful LoRA Loader now outputs loaded LoRA names/weights, which can be passed to the Name-Based LoRA Loader node to affect multiple nodes simultaneously. Example workflow uploaded.
>   

> ### Update Date: **2025.08.22**
>
> - #### All inputs of Powerful LoRA Loader node are now optional.
>   
> - #### Fixed all UI bugs of Powerful LoRA Loader and Select Text V3 nodes!!
>   

> ### Update Date: **2025.08.19**
>
> - #### Fixed some bugs and optimized functions in Tagged Prompt node.
>   
> - #### Text-to-Image and Text Watermark nodes now support transparency in all modes (not just fullscreen).
>   
> - #### Added folder support to Powerful LoRA Loader node. You can now organize LoRAs in folders. Only empty folders can be deleted. Folder styles are customizable.
>   
> - #### Since LoRA nodes have folder support, Select Text V3 also got it!
>

> ### Update Date: **2025.08.16**
>
> ### Major Update!!
> 
> - #### Text Line node can now randomize multiple lines at once.
>   
> - #### LoRA Parsing node now supports tree-folder structures.
> - #### Added Select Text V3 node: add new text boxes dynamically, each with toggle/delete buttons and custom names. Outputs combined active texts.
>   
> - #### Added Powerful LoRA Loader node (inspired by RG).
>   
>   * Features: tree-folder LoRA structure, hover image preview, outputs preset txt prompts. Dynamically add LoRAs like RG’s loader. Supports naming/custom text stored in workflow.
>     
>   * Resizable UI. Supports quick toggle/delete, draggable with lock option.
>     
>   * Known bug: After refreshing, node resets visually but data remains intact. Clicking refresh updates restores it.
>

> ### Update Date: **2025.08.14**
> 
> - #### Added “Other” category.
>   
> - #### Added Rotate Image node.
>   
> - #### Added Bridge Preview Image node.
>   
> - #### Merge Image node now supports adjusting foreground opacity.
>   
> - #### Desktop Pet saves last position.
>   
> - #### Random Text Weight node added text box.
>   
> - #### Text Watermark/Text Image nodes now support outline. Empty color = transparent, “ZML” = random color. Transparent watermarks don’t affect visibility and are harder to remove.
>

> ### Update Date: **2025.08.11**
> 
> - #### Updated Drawing node.
>   

> ### Update Date: **2025.08.08**
> 
> - #### Added Tagged Prompt Loader node (similar to old Weilin). Rewritten in JS. Supports batch txt import (format “Chinese,English”). Semi-finished.
>

> ### Update Date: **2025.08.07**
> 
> - #### Added Floating Ball!! Interactive! Default = PNG, Running = GIF, Double-click changes image and plays sound. Hover = breathing effect. Right-click = settings. Entertainment-only feature (customizable via replacing files).
>   
> - #### Added Simple Save Image node (clean UI, only 3 options: mode, path, store text).
>   
> - #### Fixed small bugs and optimizations.
>

> ### Update Date: **2025.08.06**
> 
> - #### Another major update!!
> 
> - #### Added Tagged Image Loader node (UI inspired by Weilin). Supports batch load + text block reading. Hover preview supported.
>   
> - #### Added Single Text Block Loader node.
> 
> - #### Added Audio Player node (with built-in audio).
>   
> - #### Removed LoRA Layer Control node.
>   
> - #### Optimized several nodes.
>   

> ### Update Date: **2025.08.03**
> 
> - #### Manager installation should work now. Bug fixed.
>   
> - #### Added Double Float node.
>   
> - #### Added Preset Resolution node (similar to Preset Text).
>   
> - #### Added Double Integer V3 (judgment node): compares input width/height, outputs preset resolution accordingly. Made for wan2.1 video generation.
>   
> - #### Added LoRA Metadata Parser node: auto-generates txt, log, and preview image in “zml” folder when loading LoRA.
>   
> - #### Visual Crop node now supports output at original resolution.
>   

> **Below are earlier node introductions:**
>
> 0. Enhanced Save Image node: adds support for saving text blocks into metadata, customizable naming, scaling, stripping workflow metadata.  
> 1. Enhanced Load Image node: loads single frame (even GIFs), supports transparency, reads filename/metadata.  
> 2. Load Image from Path node: supports fixed/sequential/random index loading.  
> 3. Image/GIF-to-HTML node: hides content until downloaded and opened locally.  
> 4. NAI-to-SD weight conversion node: supports tag filtering, punctuation normalization, and character removal.  
> 5. Random Text Line & Random Artist nodes: supports custom count/weights. Built-in txt of 1000 artists.  
> 6. Multiple text input/selection nodes: pre-store prompts and enable selectively.  
> 7. Resolution Limiter node: standardizes resolutions for generation or wan video frames.  
> 8. Auto-Censor node using YOLO or manual mask.  
> 9. Text Watermark node: auto line-breaks, full-screen watermarks, commercial fonts.  
> 10. Random/Predefined Integer nodes for random resolution switching.  
> 11. Based on LoRA Loader (pysss) from [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts). Supports preview, categorization, metadata linking (txt/log/image).  
> 12. Visual Crop node: manual cropping (rect/circle/path/brush).  
> 13. Limit Solid Background node: auto-remove extra pixels (supports white/green/transparent).  
> 14. Add Solid Background node: outlines subject with customizable colors.  
> 15. Merge Image node: combine 2–4 images via interactive UI. Saves internal edits. Can be used for censoring.  
> 16. Drawing node: freehand paint on images.  
> 17. Image Pause node: pauses 15s, allows output channel selection. Optimized to avoid saving placeholder images.  

</details>

## ✨ Node Update Image Showcase

<details>
<summary>Click to view updated node images</summary>

> ### Update Date: **2025.09.03**
>
> <img width="896" height="429" alt="1" src="https://github.com/user-attachments/assets/16d79123-9689-476d-a1cf-65431ba03dd0" />
> 
> <img width="909" height="778" alt="2" src="https://github.com/user-attachments/assets/eb20dc55-62e8-499b-bb8c-70f0158397c0" />
> 
> <img width="1103" height="759" alt="3" src="https://github.com/user-attachments/assets/3fdbb9d7-276a-468d-ab4b-b52b334346fd" />
>

> ### Update Date: **2025.09.02**
> 
> <img width="1782" height="869" alt="2" src="https://github.com/user-attachments/assets/54bd9449-4034-4b1b-abdc-87dfefb1a3c4" />
> 
> <img width="1048" height="925" alt="4" src="https://github.com/user-attachments/assets/1607ebfc-0e33-4818-9845-9aa366a19ee1" />
> 
> <img width="1722" height="912" alt="3" src="https://github.com/user-attachments/assets/1ff2e9ce-0d44-473d-bf42-2c9b14366265" />
> 
> <img width="1356" height="865" alt="1" src="https://github.com/user-attachments/assets/e4b1370b-130a-419c-b0c4-d94ada5283df" />
>

> #### Early node screenshots (a small portion)
>
> <img width="1632" height="875" alt="1" src="https://github.com/user-attachments/assets/77ccda88-1851-4948-a45b-2f42b46d7f53" />
>
> <img width="1601" height="784" alt="2" src="https://github.com/user-attachments/assets/21f9d0aa-834e-48dd-9384-584e0a215284" />
>
> <img width="1210" height="913" alt="3" src="https://github.com/user-attachments/assets/3359a2fd-a55a-4068-aa25-0338298b7c0b" />
>
> <img width="1698" height="862" alt="4" src="https://github.com/user-attachments/assets/059746d8-31e0-4c97-a620-6e490a6a79b4" />
> 
> <img width="1607" height="755" alt="5" src="https://github.com/user-attachments/assets/8fe91394-8874-4eb4-85dc-d7f8ce6a86da" />
>
> <img width="1719" height="745" alt="6" src="https://github.com/user-attachments/assets/2eee7e21-52a0-4d6a-bd9f-8edd52e84eff" />
>
> <img width="1261" height="762" alt="7" src="https://github.com/user-attachments/assets/a1e67136-0ed7-4664-8f3a-3de69282f71b" />
>
> <img width="982" height="893" alt="8" src="https://github.com/user-attachments/assets/dd905d68-138d-4c30-a0e2-dbdb206c11e9" />
>
> <img width="1254" height="753" alt="9" src="https://github.com/user-attachments/assets/14e6f8df-8b36-4d06-a827-8bbdef1b0e8f" />
>
> <img width="1389" height="683" alt="10" src="https://github.com/user-attachments/assets/0757a6e3-d557-4284-ad56-dcc0e004b41c" />
>
> <img width="1294" height="816" alt="11" src="https://github.com/user-attachments/assets/de9b70a5-03b0-426a-90fc-bf1d8295abf2" />
>
> <img width="1131" height="712" alt="12" src="https://github.com/user-attachments/assets/c0d253aa-96c2-4a9e-b64f-682f3908fa2e" />
>
> <img width="1196" height="639" alt="13" src="https://github.com/user-attachments/assets/c1793444-d44f-47cd-89a4-67c408cde01e" />
>
> <img width="911" height="894" alt="14" src="https://github.com/user-attachments/assets/4f666b73-f968-4182-a327-e29187ddf202" />
>
> <img width="1290" height="760" alt="15" src="https://github.com/user-attachments/assets/5a520228-fe42-49c9-a43d-e545474254f4" />
>

</details>

## ✨ Video Introduction: [Click to Visit](https://www.bilibili.com/video/BV1i4twzDELr/?spm_id_from=333.1007.0.0&vd_source=0134812498ce59b7f53810ad84889d12)

`Less introduction, no updated video, Only the Chinese language`

### Auxiliary Script Repository:

`Here are some small tools I made. Some are to assist with node usage, others are extracted node functions.`

`The scripts run independently, not within ComfyUI.`

- **https://github.com/zml-w/ZML-Image-Script/tree/main**
  

## Some Nodes and Functions Were Inspired by Others

### Referenced Code:

- **LoRA Load Node: https://github.com/pythongosssss/ComfyUI-Custom-Scripts**

### Referenced Inspirations:

- **Desktop Pet: https://github.com/11dogzi/Comfyui-ergouzi-kaiguan**

- **Tagged Prompts: https://github.com/weilin9999/WeiLin-ComfyUI-prompt-all-in-one**

- **Bridge Preview Image: https://github.com/ltdrdata/ComfyUI-Impact-Pack**

- **Powerful LoRA Loader: https://github.com/rgthree/rgthree-comfy**

## You Can Submit Issues or Ideas

`Little sister is so cute, here’s a little sister pic`

<img width="1024" height="540" alt="妹相随_6" src="https://github.com/user-attachments/assets/bc18deae-6c3c-4e70-a642-1b4210accdc3" />
