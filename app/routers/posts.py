
from ..database import engine,get_db
from fastapi import FastAPI,Response,status,HTTPException,Depends
from .. import models,schema,utils
from sqlalchemy.orm import Session


@app.get("/posts",response_model=List[schema.PostResponse])
def get_posts(db: Session = Depends(get_db)):
    posts=db.query(models.Post).all()
    # cursor.execute("""SELECT * FROM posts""")
    # posts=cursor.fetchall()
    return posts


    


@app.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schema.PostResponse)
def create_post(post: schema.PostCreate,db: Session = Depends(get_db)):
    
    new_post=models.Post(**post.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post




#Retrieving a singular post
@app.get("/posts/{id}",response_model=schema.PostResponse)
def get_post(id : int,db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""",(id,))
    # post=cursor.fetchone()
    # # post=findPost(id)
    
    post=db.query(models.Post).filter(models.Post.id==id).first()
    
    #.filter is equivalent to where
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} was not found")
    return post

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id=%s RETURNING *""",(id,))
    # post=cursor.fetchone()
    # conn.commit()
    post= db.query(models.Post).filter(models.Post.id == id)
    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
        
    post.delete(synchronize_session=False)    
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)    


@app.put("/posts/{id}",response_model=schema.PostResponse)
def update_post(id : int,post: schema.PostCreate,db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title= %s,content=%s,published=%s WHERE id= %s RETURNING *""",(post.title,post.content,post.published,id))
    # updated_post=cursor.fetchone()
    # conn.commit()
    
    post_query=db.query(models.Post).filter(models.Post.id==id)
    postQ=post_query.first()
    
    if postQ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} does not exist")
    post_query.update(post.dict(),synchronize_session=False)
    db.commit()
    #Bad way to do this
      
    return post_query.first()

