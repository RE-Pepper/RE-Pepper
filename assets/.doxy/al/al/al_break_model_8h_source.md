

# File alBreakModel.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Npc**](dir_e3d165b8bf399078b0d48c0aef5b9296.md) **>** [**alBreakModel.h**](al_break_model_8h.md)

[Go to the documentation of this file](al_break_model_8h.md)


```C++
#pragma once

#include <LiveActor/alLiveActor.h>

namespace al
{

class BreakModel : public LiveActor
{
private:
        LiveActor*             mParent;
        const sead::Matrix34f* mParentBaseMtx;
        const char*            mModelArchiveName;
        const char*            mBreakActionName;

public:
        void exeWait();
        void exeBreak();

public:
        virtual void init( const ActorInitInfo& info );
        virtual void appear();

public:
        BreakModel( LiveActor* parent, const char* name, const char* modelArchiveName, const sead::Matrix34f* parentBaseMtx = nullptr, const char* breakActionName = "Break" );
};

} // namespace al
```


