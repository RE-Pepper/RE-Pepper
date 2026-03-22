#pragma once

class GameSystem;

class RootTask /* : public sead::Task */
{
private:
        u8          super_Task[ 0x1ac ]; // not really in the mood to fix seadDelegate.h
        void*       _1b0;
        GameSystem* mGameSystem;
        void*       _1b4;
        void*       _1b8;
        void*       _1bc;

public:
        GameSystem* getGameSystem() const
        {
                return mGameSystem;
        }
};
