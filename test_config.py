#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置文件测试脚本
验证配置文件是否正确加载和使用
"""

import json
import os
from pathlib import Path

def test_config():
    """
    测试配置文件功能
    """
    print("🧪 配置文件测试")
    print("=" * 50)
    
    # 获取当前目录
    current_dir = Path(__file__).parent.absolute()
    config_path = current_dir / "config.json"
    
    # 检查配置文件是否存在
    if not config_path.exists():
        print(f"❌ 配置文件不存在: {config_path}")
        return False
    
    print(f"✅ 配置文件存在: {config_path}")
    
    # 尝试加载配置文件
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print("✅ 配置文件格式正确，成功解析JSON")
    except json.JSONDecodeError as e:
        print(f"❌ JSON格式错误: {e}")
        return False
    except Exception as e:
        print(f"❌ 读取配置文件失败: {e}")
        return False
    
    # 验证必要的配置项
    required_keys = ["imageDirectory", "filePatterns", "comparison", "output"]
    for key in required_keys:
        if key not in config:
            print(f"❌ 缺少必要的配置项: {key}")
            return False
        print(f"✅ 配置项 {key} 存在")
    
    # 验证图片目录
    img_dir = config["imageDirectory"]
    if os.path.exists(img_dir):
        print(f"✅ 图片目录存在: {img_dir}")
    else:
        print(f"⚠️ 图片目录不存在: {img_dir}")
        print("  请确保目录路径正确，或创建该目录")
    
    # 显示当前配置
    print("\n📋 当前配置内容:")
    print(f"  图片目录: {config['imageDirectory']}")
    print(f"  文件扩展名: {config['filePatterns']['fileExtension']}")
    print(f"  比较阈值: {config['comparison']['threshold']}")
    print(f"  差异图片前缀: {config['output']['diffPrefix']}")
    
    return True

if __name__ == "__main__":
    success = test_config()
    if success:
        print("\n🎉 配置文件测试通过!")
    else:
        print("\n💥 配置文件测试失败!")
        exit(1)
