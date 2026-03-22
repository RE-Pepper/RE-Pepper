

# File TrickHintPanel.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**MapObj**](dir_2096800ae80e9b320e335490a6d8aa70.md) **>** [**TrickHintPanel.h**](_trick_hint_panel_8h.md)

[Go to the documentation of this file](_trick_hint_panel_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

class TrickHintPanel : public al::MapObjActor
{
private:
        u32  _96;
        bool mPlayedSound;

public:
        void exeWait();
        void exeOn();
        void exenrv3();
        void exeOff();

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual bool receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me );

public:
        TrickHintPanel( const sead::SafeString& name );
};
```


