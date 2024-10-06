import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# DataFrame 생성
data = pd.DataFrame({
    '이름': ['영식', '철수', '영희'],
    '나이': [22, 31, 25],
    '몸무게': [75.5, 80.2, 55.1]
})

st.dataframe(data, use_container_width=True)

# Matplotlib barplot
fig, ax = plt.subplots()
ax.bar(data['이름'], data['나이'])
st.pyplot(fig)

# Seaborn barplot (새로운 fig와 ax)
fig2, ax2 = plt.subplots()
sns.barplot(x='이름', y='나이', data=data, ax=ax2, palette='Set2')
st.pyplot(fig2)

#############

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

# Matplotlib group barplot
fig3, ax3 = plt.subplots()
ax3.bar(labels, men_means, width, yerr=men_std, label='Men')
ax3.bar(labels, women_means, width, yerr=women_std, bottom=men_means, label='Women')

ax3.set_ylabel('Scores')
ax3.set_title('Scores by group and gender')
ax3.legend()

st.pyplot(fig3)

##### Barcode

code = np.array([
    1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,
    0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1,
    1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1])

pixel_per_bar = 4
dpi = 100

fig4 = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax4 = fig4.add_axes([0, 0, 1, 1])  # span the whole figure
ax4.set_axis_off()
ax4.imshow(code.reshape(1, -1), cmap='binary', aspect='auto', interpolation='nearest')

st.pyplot(fig4)
