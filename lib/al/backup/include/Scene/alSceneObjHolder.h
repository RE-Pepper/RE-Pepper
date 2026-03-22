#pragma once

namespace al
{
class ActorInitInfo;
class ISceneObj;

class SceneObjHolder
{
private:
        typedef ISceneObj* ( *CreateFunc )( int id );

        CreateFunc  mCreateFunc;
        ISceneObj** mObjs;
        int         mSize;

public:
        ISceneObj* create( int id );
        ISceneObj* getObj( int id ) const;
        bool       isExist( int id ) const;
        void       setObj( ISceneObj* obj, int id );

        void initAfterPlacementSceneObj( const ActorInitInfo& info );

public:
        SceneObjHolder( CreateFunc func, int size );
};

SceneObjHolder* getSceneObjHolder();
ISceneObj*      createSceneObj( int id );
ISceneObj*      getSceneObj( int id );
bool            isExistSceneObj( int id );
void            setSceneObj( ISceneObj* obj, int id );

} // namespace al
