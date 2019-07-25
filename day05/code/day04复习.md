#### numpy数组的拼接
  - np.hstack(t1,t2)
  - np.vstack(t1,t2)

#### Series如何创建，如何进行索引和切片
  - pd.Series([])
  - pd.Series({})  #字典的键就是Series的索引

  - s1["a"]
  - `s1[["a","c"]]`
  - `s1[1]`
  - `s2[[1,5,3]]`
  - s2[4:10]


#### DataFrame如何创建，如何进行索引和切片
  - `pd.DataFrame([[],[],[]])` #接收2维数组
  - pd.DataFrame({"a":[1,23],"c":[2,3]})
  - pd.DataFrame([{},{},{}])


#### DataFrame缺失数据处理
  - 0
    - 并不是所有的都需要处理
    - df[df==0] = np.nan
  - nan
    - pd.isnan ，pd.notnan
    - df.dropna(axis=0,how="any[all]",inplace=True)
    - df.fillna(df.mean())
    - df["A"] = df["A"].fillna(df["A"].mean())
