---
date: 2026-10-24
scope: all_tracked_stocks
symbols: 20
price_date: 2026-10-23
review: BR-20261024-ALL-001
---

# 2026-10-24 全部股票买入等级

## 结论

这是研究分级，不是下单指令。等级按“当前风险收益比 + 证据完整度 + 组合角色”排列，不是对公司质量的永久排名。2026-10-24 为非交易日，参考价使用 2026-10-23 收盘。条件未触发时不把下跌本身当成买点，也不把上涨本身当成追价理由。

未单独重写决策的标的，动作沿用 2026-07-18，等级只表示“本次不新开买入”。回避名单保持不变。

- A / A-：可以按计划小仓分批。本次没有 A 级。
- B+ / B / B-：有条件候选，或已有仓位可持有，必须遵守触发条件。
- C+ / C / C-：观察，不立即买入。
- D / E：新资金回避；E 还包含产品结构性风险。

## 等级总表

| 等级 | 股票 | 当前动作 | 参考价 | 执行要点 |
| --- | --- | --- | ---: | --- |
| B | 0700.HK 腾讯控股 | buy-candidate | 386.00 HKD | `tiny`。380-395 港元企稳才进入候选执行区；周收盘低于 360，或连续收盘低于 370，或非国际财务报告准则利润转负且自由现金流恶化同时回购停止，则失效。 |
| B- | 002594.SZ 比亚迪 | buy-candidate | 81.42 CNY | 低置信度 `tiny`。78-82 元；连续收盘低于 77.6 元，或放量同时毛利率/现金流恶化，则失效。A 股里优先重置这一只，不提高置信度。 |
| B+ | BRK.B.US Berkshire Hathaway B | hold | 542.19 USD | 持有。新资金在 510 美元或以下之前不增加；520 美元暂停线仍然有效。 |
| B+ | MSFT.US Microsoft | hold | 524.51 USD | 持有，不追。385-395 美元旧买点已远离。 |
| B | AVGO.US Broadcom | hold | 321.68 USD | 持有、不加仓。权重过高时优先降集中度。 |
| C+ | AMZN.US Amazon | watch | 248.00 USD | 等到 243-246 美元守住，或重新站上 252 美元。当前价在两段条件之间。 |
| C+ | GOOGL.US Alphabet A | watch | 320.21 USD | 先看到连续收盘回到 330 美元之上，才重新评估 `tiny`。 |
| C | 600522.SH 中天科技 | watch | 27.93 CNY | 在重新收盘站上 35.50 元之前不买。 |
| C+ | 600584.SH 长电科技 | watch | 59.78 CNY | 沿用观察。本次只更新价格。 |
| C+ | 688008.SH 澜起科技 | watch | 180.00 CNY | 沿用观察。本次只更新价格。 |
| C+ | DAL.US Delta Air Lines | watch | 76.78 USD | 沿用观察。2026-07-24 窗口已过，本次未重做油价与票价证据。 |
| C | 002050.SZ 三花智控 | watch | 35.08 CNY | 沿用观察。本次只更新价格。 |
| C | 603986.SH 兆易创新 | watch | 292.00 CNY | 沿用观察。本次只更新价格。 |
| C- | CBRS.US Cerebras | watch | 110.82 USD | 沿用观察。本次只更新价格。 |
| D | 601689.SH 拓普集团 | avoid | 44.77 CNY | 新资金回避。 |
| D | 688017.SH 绿的谐波 | avoid | 290.00 CNY | 新资金回避。 |
| D | 688322.SH 奥比中光 | avoid | 108.00 CNY | 新资金回避。价格上涨只记为反例。 |
| D | 3896.HK 金山云 | avoid | 4.46 HKD | 新资金回避。 |
| D | SPCX.US SpaceX | avoid | 147.49 USD | 新资金回避。价格回到 135 美元之上只记为反例。 |
| E | 07709.HK 南方两倍做多 SK 海力士 | avoid | 18.65 HKD | 每日两倍产品，不回补、不长期持有。 |

## 组合层面优先级

1. 新资金只有两个研究候选，且都只到 `tiny`：腾讯要先在 380-395 港元企稳；比亚迪要守住 78-82 元且不破 77.6 元，置信度低。
2. 微软和 Berkshire 是持有，不是当前买点。Berkshire 在 510 美元以上不加新资金。
3. AVGO 继续受集中度约束，321.68 美元不是加仓价。
4. Alphabet、Amazon、中天科技只观察。中天科技在收盘重新站上 35.50 元之前不买。
5. 回避名单不因奥比中光或 SpaceX 的价格回升而打开。

## 关联记录

- 批量复盘：[[60-reviews/batch/2026-10-24_ALL_RECOMMENDATIONS_REVIEW]]
- 新决策：[[40-recommendations/decisions/2026-10-24_0700.HK_DECISION]]、[[40-recommendations/decisions/2026-10-24_002594.SZ_DECISION]]、[[40-recommendations/decisions/2026-10-24_BRK.B.US_DECISION]]、[[40-recommendations/decisions/2026-10-24_MSFT.US_DECISION]]、[[40-recommendations/decisions/2026-10-24_GOOGL.US_DECISION]]、[[40-recommendations/decisions/2026-10-24_AMZN.US_DECISION]]、[[40-recommendations/decisions/2026-10-24_600522.SH_DECISION]]、[[40-recommendations/decisions/2026-10-24_AVGO.US_DECISION]]
- 原子经验：[[70-learning/lessons/lessons-log]]
