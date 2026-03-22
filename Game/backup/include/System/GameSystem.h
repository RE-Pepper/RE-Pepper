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
