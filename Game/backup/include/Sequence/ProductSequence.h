#pragma once

#include <Sequence/alSequence.h>

class ProductStageStartParam;
class StageWipeKeeper;
class ProductStateStage;
class ProductStateTitle;
class ProductStateOpening;
class ProductStateKinopioHouse;
class ProductStateMysteryBox;
class ProductStateEnding;
class ProductStateGameOverRoom;

class ProductSequence : public al::Sequence
{
private:
        ProductStageStartParam* mStageStartParam;
        void*                   _14C;
        void*                   _150;

        StageWipeKeeper*          mWipeKeeper;
        void*                     _158;
        void*                     _15C;
        ProductStateTitle*        mStateTitle;
        ProductStateOpening*      mStateOpening;
        ProductStateTitle*        mStateCourseSelect;
        ProductStateStage*        mStateStage;
        ProductStateKinopioHouse* mStateKinopioHouse;
        ProductStateMysteryBox*   mStateMysteryBox;
        ProductStateEnding*       mStateEnding;
        ProductStateGameOverRoom* mStateGameOverRoom;
        int                       _180;
        void*                     _184;
        void*                     _188;
        void*                     _18C;
        void*                     _190;

public:
        void exeTitle();
        void exeOpening();
        void exeCourseSelect();
        void exeStage();
        void exeKinopioHouse();
        void exeMysteryBox();
        void exeEnding();
        void exeGameOverRoom();
        void exeUnk1();

public:
        virtual void init();
        virtual void update();
        virtual bool isDisposable() const;

public:
        ProductSequence( const char* name );
};
