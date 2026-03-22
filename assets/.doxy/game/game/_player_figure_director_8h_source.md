

# File PlayerFigureDirector.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**PlayerFigureDirector.h**](_player_figure_director_8h.md)

[Go to the documentation of this file](_player_figure_director_8h.md)


```C++
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
```


