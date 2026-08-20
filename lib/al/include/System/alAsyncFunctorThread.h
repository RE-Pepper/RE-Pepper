#pragma once

#include <prim/seadSafeString.h>

namespace sead
{
class DelegateThread;
} // namespace sead

namespace al
{
class FunctorBase;

class AsyncFunctorThread
{
private:
        sead::DelegateThread* mSeadThread;
        const FunctorBase*    mFunctor;
        bool                  mIsDone;

public:
        void start();

        bool isDone() const
        {
                return mIsDone;
        }

public:
        virtual ~AsyncFunctorThread();

public:
        AsyncFunctorThread( const sead::SafeString& name, const FunctorBase& functor, int );
};

} // namespace al
