

# File RootTask.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**System**](dir_e1006d71d276319c0715d176f1f44d04.md) **>** [**RootTask.h**](_root_task_8h.md)

[Go to the documentation of this file](_root_task_8h.md)


```C++
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
```


