以下是关于 **Python venv 虚拟环境** 的详细使用指南，适用于 macOS 和 Linux 系统：

---

### **一、venv 虚拟环境的作用**
- **隔离依赖**：为每个项目创建独立环境，避免全局 Python 包冲突。
- **轻量级**：内置于 Python 3.3+，无需额外安装工具。
- **跨平台兼容**：适合纯 Python 项目，与 `pip` 无缝协作。

---

### **二、创建与激活虚拟环境**

#### **1. 创建虚拟环境**
```bash
# 语法：python3 -m venv <环境目录名>
python3 -m venv myenv  # 创建名为 myenv 的虚拟环境
```

#### **2. 激活虚拟环境**
```bash
# macOS/Linux
source myenv/bin/activate

# 激活后，命令行提示符会显示环境名：(myenv) $
```

#### **3. 退出虚拟环境**
```bash
deactivate
```

---

### **三、管理依赖包**

#### **1. 安装包**
```bash
# 在激活的环境中使用 pip 安装
(myenv) $ pip install numpy pandas

# 安装指定版本
(myenv) $ pip install flask==2.0.1
```

#### **2. 导出依赖列表**
```bash
(myenv) $ pip freeze > requirements.txt
```

#### **3. 从文件安装依赖**
```bash
# 在激活的环境中运行
(myenv) $ pip install -r requirements.txt
```

---

### **四、常用操作**

#### **1. 查看已安装的包**
```bash
(myenv) $ pip list
```

#### **2. 卸载包**
```bash
(myenv) $ pip uninstall package_name
```

#### **3. 删除虚拟环境**
```bash
# 直接删除环境目录
rm -rf myenv
```

---

### **五、配置 IDE 使用 venv**
- **VS Code**：  
  1. 打开项目文件夹。  
  2. 按 `Cmd + Shift + P`，输入 `Python: Select Interpreter`。  
  3. 选择虚拟环境中的 Python 路径（如 `myenv/bin/python3`）。

- **PyCharm**：  
  1. 打开项目后进入 `Preferences > Project: <项目名> > Python Interpreter`。  
  2. 点击齿轮图标，选择 `Add Interpreter > Existing Environment`。  
  3. 指定虚拟环境的 Python 路径（如 `myenv/bin/python3`）。

---

### **六、常见问题解决**

#### **1. 创建环境时报错 `command not found: python3`**
- **原因**：系统未安装 Python 3 或未正确配置。
- **解决**：  
  ```bash
  # macOS 通常预装 Python 3，若未安装可通过 Homebrew 安装
  brew install python
  ```

#### **2. 激活环境时报错 `Permission denied`**
- **原因**：虚拟环境脚本未赋予执行权限。
- **解决**：  
  ```bash
  chmod +x myenv/bin/activate
  ```

#### **3. 虚拟环境中无法找到已安装的包**
- **检查是否激活环境**：确保命令行提示符显示 `(myenv)`。
- **检查 Python 路径**：运行 `which python` 确认路径指向虚拟环境目录。

---

### **七、最佳实践**
1. **命名规范**：将虚拟环境目录命名为 `.venv` 或 `venv`，并在 `.gitignore` 中添加：
   ```text
   # .gitignore
   myenv/
   venv/
   .venv/
   ```
2. **小工具推荐**：使用 `virtualenvwrapper` 简化环境管理（需额外安装）：
   ```bash
   pip install virtualenvwrapper
   ```

---

通过 `venv`，你可以高效管理 Python 项目的依赖，确保开发环境的纯净与可复现性。