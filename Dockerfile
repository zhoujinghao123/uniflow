# 使用官方的Python运行时作为父镜像
FROM python:3.10

# 设置容器内的工作目录
WORKDIR /app

# 将requirements文件复制到容器的/app目录下
COPY requirements.txt /app/

# 安装requirements.txt中指定的所有必要依赖项
RUN pip install -r requirements.txt

# 将其余的应用程序代码复制到容器内
COPY . /app

# 暴露应用程序将运行的端口
EXPOSE 8080

# 定义运行应用程序的命令
CMD ["python", "main.py"]
