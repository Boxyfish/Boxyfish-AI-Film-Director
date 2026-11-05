# Boxyfish AI Film Director

**AI Image & Video Prompt Review and Optimization Skill**

作者：Boxyfish。此 Codex Skill 用导演、演员指导、摄影、美术和声音的判断，审核和优化 AI 生图、生视频提示词。它优先保留已确定的角色、参考图用途、动作、镜头、台词与声音；不是完整编剧或影视制作系统。

适用已有提示词检查、必要优化、多人身份和跨镜头连续性审核、生成失败原因分析。仅选择与任务相关的检查，不为增加专业感而堆词。冲突未获解决时保留双方条件、指出冲突并询问；结果标为待确认工作稿。合格内容应保持原样。

## 安装与使用

需要支持 Agent Skills 的 Codex。在 Codex 中调用 `$skill-installer`，提供仓库 `https://github.com/Boxyfish/Boxyfish-AI-Film-Director` 和目录 `skills/ai-film-prompt-director`；或在检查源码后将该目录复制到 Codex 用户级 `skills` 目录。目标目录已有同名 Skill 时，先备份并自行比较，不覆盖。Windows 中文路径请使用引号及 Unicode 支持的工具。安装后重新打开会话。

显式调用：`$ai-film-prompt-director 检查并优化这条提示词，保留已确定的全部设定，输出完整优化版。`

Codex 可以根据描述选择相关 Skill，也可能没有自动触发；关键任务请显式调用。此仓库不会自动控制普通 ChatGPT 对话或第三方视频工具。

## 示例

见 [原创示例](examples/demo.md)：包含身份图、服装图、台词、顺序和景别的合格提示词，审核后原样保留。此为原创示例，不是视频生成测试。

## 检验与限制

运行 `python scripts/check.py` 可检查核心文件和公开测试素材；另以 Codex 自带 `skill-creator/scripts/quick_validate.py` 验证格式（需要 PyYAML）。文件检查不是模型行为测试。本候选版测试状态见 `tests/RESULTS.md`。生成结果还需实际模型、参考资产、音轨及成片验证；不保证成功或自动触发。

## 更新和回退

先保留当前安装目录，比较新版本和本地改动；确认后备份再替换。出错时恢复此前的备份目录。GitHub 保存发布版本；本机 Skill 为运行副本；研究资料单独管理，不自动双向同步。版本见 `VERSION` 与 `CHANGELOG.md`。

## 许可

本公开版本采用 [MIT License](LICENSE)，版权所有 © 2026 Boxyfish。私人扩展及其资料不自动适用此许可证。
