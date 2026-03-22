#pragma once

#include <LiveActor/alLiveActor.h>
#include <container/seadPtrArray.h>

namespace al
{

class LiveActorGroup
{
private:
        const char* const         mName;
        sead::PtrArray<LiveActor> mActors;

public:
        void killAll();
        void makeActorDeadAll();

        template <typename T>
        sead::PtrArray<T>& getArray()
        {
                return reinterpret_cast<sead::PtrArray<T>&>( mActors );
        }

public:
        virtual void registerActor( LiveActor* actor );

public:
        LiveActorGroup( const char* name, int bufSize );
};

} // namespace al
