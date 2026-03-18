

# File alFunctorV0M.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Functor**](dir_0fa42dffbcd7ed2ad30fd522996e9ccf.md) **>** [**alFunctorV0M.h**](al_functor_v0_m_8h.md)

[Go to the documentation of this file](al_functor_v0_m_8h.md)


```C++
#pragma once

#include <Functor/alFunctorBase.h>

namespace al
{

template <typename T, typename F>
class FunctorV0M : public FunctorBase
{
private:
        T mParent;
        F mFuncPtr;

public:
        virtual void operator()() const
        {
                ( mParent->*mFuncPtr )();
        }

        virtual FunctorV0M* clone() const
        {
                return new FunctorV0M<T, F>( mParent, mFuncPtr );
        }

public:
        FunctorV0M( T parent, F funcPtr ) : mFuncPtr( funcPtr ), mParent( parent )
        {
        }
};

} // namespace al
```


