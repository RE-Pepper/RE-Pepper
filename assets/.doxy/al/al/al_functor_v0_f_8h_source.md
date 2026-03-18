

# File alFunctorV0F.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Functor**](dir_0fa42dffbcd7ed2ad30fd522996e9ccf.md) **>** [**alFunctorV0F.h**](al_functor_v0_f_8h.md)

[Go to the documentation of this file](al_functor_v0_f_8h.md)


```C++
#pragma once

#include <Functor/alFunctorBase.h>

namespace al
{

class FunctorV0F : public FunctorBase
{
private:
        typedef void ( *FuncType )();
        FuncType mFuncPtr;

public:
        virtual void operator()() const
        {
                mFuncPtr();
        }

        virtual FunctorBase* clone() const
        {
                return new FunctorV0F( mFuncPtr );
        }

public:
        FunctorV0F( FuncType func ) : mFuncPtr( func )
        {
        }
};

} // namespace al
```


