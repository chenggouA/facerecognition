# retinaface + facenet 实现人脸识别

打包成模块的方式，易于调用

如
```
    main.py
```

`face/face_dataset/` 存放带匹配的人脸图像 

使用`face/encoding.py` 对这些图像进行编码，编码后的数据存放在 `face/model_data/`

`face/config.py` 是对模型的配置文件
