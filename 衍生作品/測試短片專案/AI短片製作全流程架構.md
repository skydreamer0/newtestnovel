# 《鼠鑄》測試短片：AI 全流程製作架構

基於專家經驗與現有成熟工作流，我們為《鼠鑄》的測試短片建立以下從 0 到 1 的生成式 AI (AIGC) 製作架構。這套流程將傳統動畫製作的繁雜步驟，精簡為四個核心階段，並在每個節點保持人類導演的「審美與故事把控」。

---

## 階段一：前期準備與 AI 腳本化 (Pre-production & AI Scripting)
**核心邏輯**：資料餵養 → 拆解元素 → 結構化分鏡
**使用工具**：Claude / ChatGPT 等語言大模型 (LLM)

1. **資料搜集與世界觀同步**
   * 提煉原著《鼠鑄》核心世界觀（鼠籠城、廢鐵、賽博龐克、神性科技）。
   * 將企劃案的情境引言與歌詞，轉換為明確的畫面需求。
2. **AI 溝通技巧 (Prompt Engineering for Scripts)**
   * **賦予身份**：要求 LLM 扮演「動畫短片導演」或「分鏡師」。
   * **拆解場景**：請 AI 將歌詞與旁白逐句拆解為「鏡頭語言」、「畫面主體」與「氛圍描述」。
3. **產出物**：
   * 完整的 `企劃案.md` 與分鏡表。
   * **(目前已完成)**：包含 7 個關鍵鏡頭的基礎規劃。

---

## 階段二：AI 圖像生成 (AI Image Generation)
**核心邏輯**：文本引導 → 視覺化 → 反覆測試與篩選 (測試至滿意為止)
**使用工具**：Midjourney (v5.2 / v6.0)

1. **定義 Prompt 公式**
   * 參照電影級高質量生成公式，避免空泛描述。
   * **公式參考**：`[主體描述], expansive and intimate visual storytelling, epic sci-fi vision, [攝影風格與底片質感 e.g. Kodak Vision3 500T] --ar 21:9 --style raw --v 6.0`
2. **角色與風格連貫性 (Consistency)**
   * **角色鎖定**：使用固定的容貌特徵詞（如目前的 `same character, asian male, glowing blue cybernetic interface eyes, mechanical prosthetic arm...`）。
   * 透過 `--cref` (Character Reference) 或 `--sref` (Style Reference) 指令進一步強化連貫性。
3. **產出物**：
   * 每個關鍵鏡頭的高畫質靜態關鍵影格 (Keyframes)。
   * 約 20% 的時間會花在人工挑選最符合《鼠鑄》壓迫與工業恐怖感的畫面。
   * 儲存至 `assets/` 資料夾。

---

## 階段三：影片動態生成 (AI Video Generation)
**核心邏輯**：圖生影片 (Image-to-Video) → 鏡頭運動控制 → 篩選可用片段
**使用工具**：Runway Gen-2 / AnimateDiff / Luma Dream Machine

1. **圖生影片 (Image to Video)**
   * 將 Phase 2 產出的完美靜態圖匯入影片生成 AI。
2. **導演模式控制 (Director Mode / Camera Motion)**
   * 精準控制鏡頭參數（如：`Zoom in`, `Pan Right`, `Tilt up`），確保畫面動態符合音樂節奏（例如主歌緩慢推進，副歌爆發）。
   * 使用特定的 Motion Prompt，例如：`slow drifting fog, subtle neon flickering, raindrops falling`。
3. **產出物**：
   * 每個鏡頭數個 3~4 秒的影片素材（需人工篩選去除結構崩壞變形的片段）。
   * 這些將構成短片的核心視覺素材。

---

## 階段四：後期剪輯與合成 (Post-production & Editing)
**核心邏輯**：畫面組裝 → 色彩統一 → 特效疊加 → 聲畫同步
**使用工具**：DaVinci Resolve / Adobe Premiere / Adobe After Effects (AE)

1. **粗剪與聲畫對齊**
   * 將生成的 AI 影片放入 DaVinci 軌道，精確對齊引言旁白與《死寂頻率》歌曲的 BPM（節奏點）。
2. **統一調色 (Color Grading)**
   * AI 生成的片段可能有色差，需統一調整為高對比的「黑 x 霓虹紅/藍」賽博龐克色調。
3. **特效與字體疊加 (VFX & Typography)**
   * 在 AE 中製作：
     * **Glitch / 故障藝術 / 掃描線特效**，增強技術崩壞感。
     * 動態設計：讓歌詞以「終端機代碼」或「報錯視窗」形式跳出。
4. **產出物**：
   * 完整的《鼠鑄》概念短片 (MP4 高畫質最終輸出)。

---

## 總結
這套「AI 動畫製片管線」大幅壓縮了傳統美術設計與3D算圖的時間。我們的下一步，就是專注在 **階段二 (AI 圖像生成)**，待 API 資源恢復後，逐步為 7 個關鍵鏡頭打磨出完美的靜態底圖。
