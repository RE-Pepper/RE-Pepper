

# File alBreakModel.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Npc**](dir_43489f5cd47c3c88012e1bbb9faf90cc.md) **>** [**alBreakModel.h**](al_break_model_8h.md)

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


