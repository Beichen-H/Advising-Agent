import os
import shutil
from rag_client import RAGClient

def rebuild_database():
    """重建向量数据库"""
    print("🔄 Rebuilding vector database...")
    
    # 删除旧的数据库
    persist_dir = "./data/chroma_db"
    if os.path.exists(persist_dir):
        print(f"🗑️  Removing old database at {persist_dir}")
        shutil.rmtree(persist_dir)
    
    # 重新创建
    client = RAGClient()
    print("✅ Database rebuilt successfully!")

if __name__ == "__main__":
    rebuild_database()
