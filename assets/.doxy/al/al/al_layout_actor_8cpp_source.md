

# File alLayoutActor.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Layout**](dir_17ff0a3ba0f744361034893725301bda.md) **>** [**alLayoutActor.cpp**](al_layout_actor_8cpp.md)

[Go to the documentation of this file](al_layout_actor_8cpp.md)


```C++
#include <Layout/alLayoutActor.h>

namespace al
{

LayoutActor::LayoutActor( const char* name )
    : mName( name ), mNerveKeeper( nullptr ), mAudioKeeper( nullptr ), mEffectKeeper( nullptr ),
      _20( nullptr ), _24( nullptr ), _28( nullptr ), mIsAlive( false )
{
}

NerveKeeper* LayoutActor::getNerveKeeper() const
{
        return mNerveKeeper;
}

void LayoutActor::appear()
{
        mIsAlive = true;
        calcAnim();
}

void LayoutActor::kill()
{
        if ( getEffectKeeper() )
                getEffectKeeper()->deleteAndClearEffectAll();
        mIsAlive = false;
}

AudioKeeper* LayoutActor::getAudioKeeper() const
{
        return mAudioKeeper;
}

EffectKeeper* LayoutActor::getEffectKeeper() const
{
        return mEffectKeeper;
}

void LayoutActor::control()
{
}

void LayoutActor::initNerve( const Nerve* nerve, int step )
{
        mNerveKeeper = new NerveKeeper( this, nerve, step );
}

} // namespace al
```


