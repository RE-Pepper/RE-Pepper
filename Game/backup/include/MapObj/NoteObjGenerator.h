#pragma once

#include <MapObj/alMapObjActor.h>

namespace al
{
class LiveActorGroup;
}

class NoteObjGenerator : public al::MapObjActor
{
private:
        al::LiveActorGroup* mNoteObjGroup;
        void*               _64;
        float               _68;
        float               _6C;
        void*               _70;
        int                 _74;
        bool                _78;
        float               _7C;
        void*               _80;
        bool                _84;

public:
        void exeWait();
        void exeMove();
        void exeDisappear();
        void exeSuccess();

public:
        NoteObjGenerator( const sead::SafeString& name );
};
