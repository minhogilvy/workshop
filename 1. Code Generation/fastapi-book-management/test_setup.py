"""
Simple test script to verify the FastAPI application setup.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    """Test that all modules can be imported successfully."""
    try:
        from app.main import app
        from app.core.config import get_settings
        from app.models import User, Book, UserBookStatus
        from app.schemas import UserCreate, BookCreate, Token
        from app.services import AuthService, BookService, UserBookService

        print("✅ All imports successful!")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_settings():
    """Test settings configuration."""
    try:
        from app.core.config import get_settings
        settings = get_settings()

        print(f"✅ Settings loaded: {settings.APP_NAME} v{settings.APP_VERSION}")
        return True
    except Exception as e:
        print(f"❌ Settings error: {e}")
        return False

def test_app_creation():
    """Test FastAPI app creation."""
    try:
        from app.main import app

        # Check if app is created
        assert app is not None
        assert hasattr(app, 'title')

        print(f"✅ FastAPI app created: {app.title}")
        return True
    except Exception as e:
        print(f"❌ App creation error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Book Management System Setup...")
    print("-" * 50)

    tests = [
        ("Import Test", test_imports),
        ("Settings Test", test_settings),
        ("App Creation Test", test_app_creation),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name}...")
        if test_func():
            passed += 1
        else:
            print(f"   Test failed!")

    print("\n" + "=" * 50)
    print(f"📊 Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! The application is ready to run.")
        print("\n📝 Next steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Set up environment: cp .env.example .env")
        print("3. Run the application: uvicorn app.main:app --reload")
        print("4. Visit http://localhost:8000/docs for API documentation")
    else:
        print("⚠️  Some tests failed. Please check the setup.")
        sys.exit(1)