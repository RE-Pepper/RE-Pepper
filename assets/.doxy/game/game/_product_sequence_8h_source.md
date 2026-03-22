

# File ProductSequence.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Sequence**](dir_add35431d27bbd5f0559725cdc453615.md) **>** [**ProductSequence.h**](_product_sequence_8h.md)

[Go to the documentation of this file](_product_sequence_8h.md)


```C++
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
```


