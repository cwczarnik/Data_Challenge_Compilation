from sklearn.cross_validation import train_test_split
from sklearn.metrics import precision_recall_curve, roc_curve
   
def rfc_model_analysis(model,X,Y):
    # Model Must be a Random Forest Classifier
    
    model.fit(X_train,y_train)
    predict = model.predict_proba(X_test)[:,1]
    prec, rec, thresh_ = precision_recall_curve(y_test,predict)
    fpr,tpr, thresh2 = roc_curve(y_test,predict)
    plt.figure(figsize=(10,5))
    plt.subplot(1, 2, 1)
    plt.plot(rec,prec)

    plt.xlabel('recall')
    plt.ylabel('precision')
    plt.subplot(1,2,2)
    plt.plot(fpr,tpr)
    plt.plot([1,0], [1,0], 'k--', lw=2)
    plt.xlabel('fpr')
    plt.ylabel('tpr')
    plt.show()

    # F1 = 2 * (prec * rec) / (prec + rec)
    thresh = list(thresh)
    # thresh.append(1)
    plt.subplot(1,2,1)
    plt.plot(thresh2,tpr)
    plt.title('TPR Versus Threshold')
    plt.ylabel('tpr')
    plt.xlabel('Threshold')
    plt.show()

    # F1 = 2 * (prec * rec) / (prec + rec)
    thresh = list(thresh2)
    # thresh.append(1)
    plt.subplot(1,2,2)
    plt.plot(thresh,fpr)
    plt.title('FPR Versus Threshold')
    plt.ylabel('fpr')
    plt.xlabel('Threshold')
    plt.show()
    
    sort_index = np.argsort(model.feature_importances_)
    importances = model.feature_importances_
    sort_importances = importances[sort_index]
    # plt.subplot(1,2,1)
    fig, ax = plt.subplots(figsize =(5,10))
    ind = np.array(range(len(X_test.columns[sort_index])))+.7
    # plt.figure(figsize = (10,20))

    plt.barh(ind,sort_importances);
    ax.set_yticks(ind + .3);
    ax.set_yticklabels((X_test.columns[sort_index]))
    plt.title('Feature Importance')

    print("At threshold = 0.5")
    print metrics.classification_report(y_test,y_pred>0.5)
    print 'accuracy: ',metrics.accuracy_score(y_test,y_pred>0.5)
    
    return(model)