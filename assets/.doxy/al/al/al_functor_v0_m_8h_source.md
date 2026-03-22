

# File alFunctorV0M.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Functor**](dir_4b1618e0f87ca3a70fa89f8b6dfa1b0c.md) **>** [**alFunctorV0M.h**](al_functor_v0_m_8h.md)

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


