

# File ItemHolder.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**MapObj**](dir_2096800ae80e9b320e335490a6d8aa70.md) **>** [**ItemHolder.h**](_item_holder_8h.md)

[Go to the documentation of this file](_item_holder_8h.md)


```C++
#pragma once

#include <Scene/alISceneObj.h>
#include <container/seadPtrArray.h>

namespace al
{
class LiveActor;
}
class CoinCharger;

class ItemHolder : public al::ISceneObj
{
private:
        sead::PtrArray<al::LiveActor>* mCoins;
        sead::PtrArray<al::LiveActor>* mCountUpCoins;
        sead::PtrArray<al::LiveActor>* mFireFlowers;
        sead::PtrArray<al::LiveActor>* mKinokoOneUps;
        sead::PtrArray<al::LiveActor>* mFastKinokoOneUps;
        sead::PtrArray<al::LiveActor>* mKinokoPoisons;
        sead::PtrArray<al::LiveActor>* mFastKinokoPoisons;
        sead::PtrArray<al::LiveActor>* mKinokos;
        sead::PtrArray<al::LiveActor>* mFastKinokos;
        sead::PtrArray<al::LiveActor>* mBoomerangFlowers;
        sead::PtrArray<al::LiveActor>* mPatapataWings;
        sead::PtrArray<al::LiveActor>* mAssistItems;
        sead::PtrArray<al::LiveActor>* mSuperLeaves;
        sead::PtrArray<al::LiveActor>* mSpecialSuperLeaves;
        sead::PtrArray<al::LiveActor>* mSuperStars;
        sead::PtrArray<al::LiveActor>* mClocks;
        sead::PtrArray<al::LiveActor>* mCollectCoins;
        sead::PtrArray<al::LiveActor>* mKickKouras;
        CoinCharger*                   mCoinCharger;
        void*                          _50;
        void*                          _54;
        void*                          _58;

public:
        void initCoinCharger( const al::LayoutInitInfo& info );

        virtual const char* getSceneObjName() const
        {
                return "ItemHolder";
        }

public:
        ItemHolder( int, int, int );
};
```


