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
