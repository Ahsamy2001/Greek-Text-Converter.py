import pandas as pd

# بيانات جدول الحروف — أكمل القوائم حسب الجدول الذي تريد
data = {
    "English Upper": ["A","B","C","D"],
    "English Lower": ["a","b","c","d"],
    "Greek Upper":  ["Α","Β","","Δ"],
    "Greek Lower":  ["α","β","","δ"],
}

# إنشاء DataFrame
df = pd.DataFrame(data)

# تصدير إلى ملف CSV
df.to_csv("English-Greek-Latin_Mapping_Table.csv", index=False, encoding="utf-8")
