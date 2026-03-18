

# File alClippingDirector.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Clipping**](dir_b42721b03f0382f09cda06110232e739.md) **>** [**alClippingDirector.h**](al_clipping_director_8h.md)

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


