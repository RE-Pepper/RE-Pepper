

# File alWipeSimple.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Layout**](dir_df428175ad75013516ece83f85ae05d3.md) **>** [**alWipeSimple.h**](al_wipe_simple_8h.md)

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


