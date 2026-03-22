#pragma once

namespace al
{

class ClippingActorInfoList;
class LiveActor;

class ClippingActorHolder
{
private:
        int                    _0;
        int                    _4;
        ClippingActorInfoList* _8;
        ClippingActorInfoList* _C;
        ClippingActorInfoList* _10;
        ClippingActorInfoList* _14;

public:
        void invalidateClipping( LiveActor* actor );
        void validateClipping( LiveActor* actor );

public:
        ClippingActorHolder( int );
};

} // namespace al
