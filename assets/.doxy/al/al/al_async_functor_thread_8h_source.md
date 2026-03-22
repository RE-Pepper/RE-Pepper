

# File alAsyncFunctorThread.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**System**](dir_61ffa07cfbda06360481d678005eeea2.md) **>** [**alAsyncFunctorThread.h**](al_async_functor_thread_8h.md)

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


