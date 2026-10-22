#pragma once

#include <LiveActor/alLiveActor.h>
#include <Scene/alISceneObj.h>

class CoinRotator : public al::LiveActor, public al::ISceneObj
{
private:
        float mRotateY;
        u8    _68[ 0x64 ];

public:
        float getRotateY()
        {
                return mRotateY;
        }

public:
        virtual const char* getSceneObjName() const;
        virtual void        initAfterPlacementSceneObj( const al::ActorInitInfo& info );

        virtual void movement();

public:
        CoinRotator();
};

namespace rp
{

void  createCoinRotator();
float getCoinRotateY();

} // namespace rp
