

# File GameSystem.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**System**](dir_e1006d71d276319c0715d176f1f44d04.md) **>** [**GameSystem.h**](_game_system_8h.md)

[Go to the documentation of this file](_game_system_8h.md)


```C++
#pragma once

#include <Nerve/alNerveExecutor.h>

namespace al
{
class LayoutKit;
class MessageSystem;
class Sequence;
} // namespace al
class CourseList;

class GameSystem : public al::NerveExecutor
{
        friend class ApplicationFunction;

private:
        al::Sequence*      mCurrentSequence;
        void*              _C;
        void*              _10;
        al::LayoutKit*     mLayoutKit;
        void*              _18;
        al::MessageSystem* mMessageSystem;
        void*              _20;
        void*              _24;
        CourseList*        mCourseList;
        void*              _2C;
        void*              _30;
        void*              _34;

public:
        CourseList* getCourseList() const
        {
                return mCourseList;
        }

public:
        virtual void init() {};
        virtual void movement() {};
        virtual void v6() {};
        virtual void v7() {};
        virtual void v8() {};

public:
        GameSystem();
};
```


