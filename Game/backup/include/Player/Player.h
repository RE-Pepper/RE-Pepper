#pragma once

class IUsePlayerAnimator;
class PlayerActionGraph;
class PlayerAnimator;
class PlayerAudio;
class PlayerFigureDirector;
class PlayerProperty;
class PlayerTrigger;

class Player
{
private:
        PlayerProperty*       mPlayerProperty;
        void*                 _4;
        void*                 _8;
        void*                 _C;
        void*                 _10;
        void*                 _14;
        void*                 _18;
        IUsePlayerAnimator*   mUsePlayerAnimator;
        PlayerTrigger*        mPlayerTrigger;
        void*                 _24;
        void*                 _28;
        void*                 _2C;
        void*                 _30;
        void*                 _34;
        void*                 _38;
        void*                 _3C;
        PlayerFigureDirector* mFigureDirector;
        void*                 _44;
        PlayerActionGraph*    mActionGraph;
        void*                 _4C;
        void*                 _50;
        void*                 _54;
        void*                 _58;
        void*                 _5C;
        void*                 _60;
        void*                 _64;
        void*                 _68;
        void*                 _6C;
        void*                 _70;
        void*                 _74;
        void*                 _78;
        void*                 _7C;
        PlayerAudio*          mPlayerAudio;
        void*                 _84;
        void*                 _88;
        void*                 _8C;
        void*                 _90;
        void*                 _94;
        void*                 _98;
        void*                 _9C;
        void*                 _A0;
        void*                 _A4;
        void*                 _A8;
        void*                 _AC;
        void*                 _B0;
        void*                 _B4;
        void*                 _B8;
        void*                 _BC;
        void*                 _C0;
        void*                 _C4;
        void*                 _C8;
        void*                 _CC;
        void*                 _D0;
        void*                 _D4;
        void*                 _D8;
        void*                 _DC;
        void*                 _E0;
        void*                 _E4;
        void*                 _E8;
        void*                 _EC;
        void*                 _F0;
        void*                 _F4;

public:
        PlayerProperty* getProperty()
        {
                return mPlayerProperty;
        }
};
