

# File alFunctorBase.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Functor**](dir_0fa42dffbcd7ed2ad30fd522996e9ccf.md) **>** [**alFunctorBase.h**](al_functor_base_8h.md)

[Go to the documentation of this file](al_functor_base_8h.md)


```C++
#pragma once

namespace al
{

class FunctorBase
{
public:
        virtual void         operator()() const = 0;
        virtual FunctorBase* clone() const      = 0;
};

} // namespace al
```


