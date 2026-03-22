#include <LiveActor/alLiveActorGroup.h>

namespace al
{

#ifdef NON_MATCHING
LiveActorGroup::LiveActorGroup( const char* name, int bufSize )
    : mName( name )
{
        mActors.allocBufferInline( bufSize );
}
#endif

void LiveActorGroup::registerActor( LiveActor* actor )
{
        mActors.pushBack( actor );
}

void LiveActorGroup::killAll()
{
        for ( int i = 0; i < mActors.size(); i++ )
                mActors.unsafeAt( i )->kill();
}

void LiveActorGroup::makeActorDeadAll()
{
        for ( int i = 0; i < mActors.size(); i++ )
                mActors.unsafeAt( i )->makeActorDead();
}

} // namespace al
