

# File alAsyncFunctorThread.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**System**](dir_29a5069bbf312f731d8cb4e203fae6bc.md) **>** [**alAsyncFunctorThread.h**](al_async_functor_thread_8h.md)

[Go to the documentation of this file](al_async_functor_thread_8h.md)


```C++
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
```


