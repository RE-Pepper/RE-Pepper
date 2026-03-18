

# File alWipeSimple.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Layout**](dir_71ac96d9eee999c5231127773bfe6eda.md) **>** [**alWipeSimple.h**](al_wipe_simple_8h.md)

[Go to the documentation of this file](al_wipe_simple_8h.md)


```C++
#pragma once

#include <Layout/alLayoutActor.h>

namespace al
{

class WipeSimple : public al::LayoutActor
{
        int _30;

public:
        void exeClose();
        void exeWait();
        void exeOpen();

        bool isCloseEnd() const;

public:
        virtual void appear();

public:
        WipeSimple( const char* name, const char* archive, const LayoutInitInfo& info, const char* suffix = nullptr );
};

} // namespace al
```


