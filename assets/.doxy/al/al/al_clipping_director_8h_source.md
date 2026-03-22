

# File alClippingDirector.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Clipping**](dir_7e8c68cf19e0ef7d7545051dcecbf0eb.md) **>** [**alClippingDirector.h**](al_clipping_director_8h.md)

[Go to the documentation of this file](al_clipping_director_8h.md)


```C++
#pragma once
#include <Execute/alExecuteDirector.h>

namespace al
{
class ClippingActorHolder;

class ClippingDirector : public IUseExecutor
{
private:
        int                  _4;
        ClippingActorHolder* mClippingActorHolder;
        void*                _C;
        void*                _10;

public:
        void endInit();

        ClippingActorHolder* getClippingActorHolder()
        {
                return mClippingActorHolder;
        }

public:
        virtual void execute();

public:
        ClippingDirector( int );
};

} // namespace al
```


