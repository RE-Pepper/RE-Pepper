#pragma once

#include <Layout/alLayoutActor.h>

class FileInfo : public al::LayoutActor
{
private:
        class FileSelect* mFileSelect;
        int               _34;
        int               _38;
        int               _3C;
        bool              _40;
        void*             _44;
        bool              _48;

public:
        virtual void appear();

public:
        FileInfo( const al::LayoutInitInfo& info, FileSelect* fileSelect );
};
