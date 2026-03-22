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
