#pragma once

#include "Player/PlayerAudio.h"

enum EPlayerFigure
{
        EPlayerFigure_Normal,
        EPlayerFigure_Mini,
        EPlayerFigure_Fire,
        EPlayerFigure_RaccoonDog,
        EPlayerFigure_Boomerang,
        EPlayerFigure_RaccoonDogSpecial,
        EPlayerFigure_RaccoonDogWhite
};

// has table of which Figure to switch to when damagaed
class PlayerFigureLoss
{
public:
        virtual void update( EPlayerFigure*, const EPlayerFigure& );
};

class PlayerFigureTransformer
{
};

class PlayerFigureDirector
{
private:
        EPlayerFigure    mLastFigure;
        EPlayerFigure    mFigure;
        void*            _8;
        void*            _C;
        bool             mHasFigureChanged;
        bool             _11;
        IUsePlayerAudio* mAudioUser;

public:
        void change( const EPlayerFigure& );
        void lose();
        void set( const EPlayerFigure& );

        EPlayerFigure getFigure() const
        {
                return mFigure;
        }
};
