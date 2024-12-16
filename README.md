# 创意魔术基准 | Creative Magic Benchmark

## 1. 字段解释

1. Magics (魔术):
    - ID (魔术的唯一标识符)
    - Setting (魔术的设置):
        - Location (魔术的地点)
        - Objects (魔术的道具)
        - Imagepath (魔术的图片路径, 可选)
    - Schemes (魔术的方案列表):
        - ID (方案的唯一标识符)
        - Name (方案的名称)
        - Setter (出题人视角的总结)
        - Audience (观众视角的步骤)
        - Performer (表演者视角的步骤)

2. Designs (出题人视角的设计思路):
    - Name (设计的名称)
    - Description (设计的描述)

3. Views (观众视角的观赏效果):
    - Name (效果的名称)
    - Description (效果的描述)

4. Techs (表演者视角的手法动作):
    - Name (手法的名称)
    - Description (手法的描述)

## 2. 综合得分公式

为了综合评估模型，引入一个包括 **出题人 (Setter)**、**观众 (Audience)** 和 **表演者 (Performer)** 三项的综合得分公式。每一项都考虑了收敛性约束和发散性约束。

$$
\text{Score} = \alpha \times \text{Score}_{\text{S}} + \beta \times \text{Score}_{\text{A}} + \gamma \times \text{Score}_{\text{P}}
$$

---

## 3. 各项得分的计算方法

### $\text{Score}_{\text{S}}$

- **收敛性约束：** 评估方案是否符合出题人视角指定的对象和地点，输出 float。
- **发散性约束：** 评估方案中超出 **常规设计 (setter_design)** 的新思路，输出 float。

**公式：**

$$
\text{Score}_{\text{S}} =  \frac{1}{|Y_t|} \sum_{y^t_i \in Y_t}  \left[\underbrace{f_{\text{S}}(y^t_i)}_{\text{收敛性}}   \times \underbrace{\left( \frac{|D^t_i \setminus D_{\text{S}}|}{|D^t_i|} \right)}_{\text{发散性}}\right]
$$

### $\text{Score}_{\text{A}}$

- **收敛性约束：** 评估方案是否符合观众视角的观赏性，输出 float。
- **发散性约束：** 评估方案中超出 **常规观赏 (audience_view)** 的新效果，输出 float。

**公式：**

$$
\text{Score}_{\text{A}} =  \frac{1}{|Y_t|} \sum_{y^t_i \in Y_t} \left[\underbrace{f_{\text{A}}(y^t_i)}_{\text{收敛性}}   \times \underbrace{\left( \frac{|V^t_i \setminus V_{\text{A}}|}{|V^t_i|} \right)}_{\text{发散性}}\right]
$$

### $\text{Score}_{\text{P}}$

- **收敛性约束：** 评估方案是否符合表演者视角的表演难度，输出 float。
- **发散性约束：** 评估方案中超出 **常规手法 (performer_tech)** 的新手法，输出 float。

**公式：**

$$
\text{Score}_{\text{P}} =  \frac{1}{|Y_t|} \sum_{y^t_i \in Y_t} \left[\underbrace{f_{\text{P}}(y^t_i)}_{\text{收敛性}}  \times \underbrace{\left( \frac{|T^t_i \setminus T_{\text{P}}|}{|T^t_i|} \right)}_{\text{发散性}}\right]
$$

**其中：**

- $Y_t$ 是第 $t$ 个魔术的方案集合，$y^t_i$ 是第 $t$ 个魔术的第 $i$ 个方案
- $f_\text{S},f_\text{A},f_\text{P}$ 是调用 API 评判收敛性的函数
- $D^t_i$ 是调用 API 提取的第 $t$ 个魔术的第 $i$ 个方案的出题人视角的设计集合，$D_{\text{S}}$ 是常规设计集合
- $V^t_i$ 是调用 API 提取的第 $t$ 个魔术的第 $i$ 个方案的观众视角的效果集合，$V_{\text{A}}$ 是常规观赏集合
- $T^t_i$ 是调用 API 提取的第 $t$ 个魔术的第 $i$ 个方案的表演者视角的手法集合，$T_{\text{P}}$ 是常规手法集合

## 4. 细节

- 如何检查某个魔术流程方案的设计思路是否属于预设的常规设计思路？

    使用 spaCy 模型，将设计思路和常规设计思路的 Name 和 Description 字段分别进行近义词计算，如果相似度大于阈值，则认为属于常规设计思路。

- 如何处理输入的图片？

    使用 ViLT 模型，将图片中的对象提取出来，加入到魔术的 Objects 属性中。

- 如何解决 LLM 不稳定的问题？

    使用多次调用 API 取平均值的方法。
