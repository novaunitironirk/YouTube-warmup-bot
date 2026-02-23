from session_manager import SessionManager
from warmup_engine import WarmupEngine

def main():
    session = SessionManager()
    session.start()

    engine = WarmupEngine(session.driver)
    engine.run()

if __name__ == "__main__":
    main()